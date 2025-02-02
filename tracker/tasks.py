from datetime import datetime, timedelta

from celery import shared_task

from tracker.models import Habits

from .services import send_message


@shared_task
def habit_to_do_reminder():
    """Проверяет необходимость выполнения привычки. Возвращает сообщение-напоминание и id Телеграмма пользователя."""
    result = []
    today = datetime.now().date()
    habits = Habits.objects.filter(is_pleasant=False)
    habits = habits.select_related('user')
    for habit in habits:
        # проверяем необходимость выполнения привычки сегодня
        if (today - habit.last_action_date).days == habit.period:
            # проверяем пришло ли время выполнения привычки
            if datetime.combine(
                datetime.now(), habit.time
            ) - datetime.now() <= timedelta(minutes=10):
                message = f"Напоминаем, вам следует {habit.action} в {habit.place} в {habit.time}."
                tg_id = habit.user.tg_id
                result.append((message, tg_id))
                # обновляем дату последнего действия привычки
                habit.last_action_date = today
                habit.save()
    # в цикле проходимся по result и отправляем напоминания через телеграм
    if result:
        for message, tg_id in result:
            send_message(text=message, chat_id=tg_id)
