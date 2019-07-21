FROM python:alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /usr/app

COPY ./requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
COPY ./ ./

CMD ["python", "wsgi.py"]