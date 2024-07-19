import python_weather

import asyncio
import os

async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.client.Client(locale = python_weather.enums.Locale.RUSSIAN) as client:


        # Введите название городе
        weather = await client.get('*')

        # Прогноз на 3 дня
        for daily in weather.daily_forecasts:
            print(f'Дата - {daily.date}  Мин. температура - {daily.lowest_temperature} Макс. температура - {daily.highest_temperature}')

            # Прогноз на каждые 3 часа
            for hourly in daily.hourly_forecasts:
                print(f' --> {hourly.time} \nТемпература  - {hourly.temperature}C \nОсадки - {hourly.description}')


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())