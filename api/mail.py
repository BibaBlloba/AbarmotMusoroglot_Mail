import subprocess
from subprocess import call

import psycopg2
from fastapi import APIRouter, Body, HTTPException

from config import settings

router = APIRouter(prefix="/mail")


@router.post("")
async def create_mail(
    username: str = Body(),
    passwd: str = Body(),
):
    if passwd != settings.PASSWD:
        raise HTTPException(401)

    # Подключаемся к базе данных
    connection = psycopg2.connect(
        dbname=settings.DBNAME,
        user=settings.USER,
        password=settings.PASSWORD,
        host=settings.HOST,
        port=settings.PORT,
    )

    result = subprocess.run(
        f"./create_mail_user_SQL.sh {username}@akeka.ru poi",
        capture_output=True,
        text=True,
        shell=True,
    )
    output = result.stdout

    cursor = connection.cursor()
    insert_query = output

    cursor.execute(insert_query)
    connection.commit()
    connection.close()
