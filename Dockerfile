FROM python:3.9-slim-bullseye
WORKDIR /code
ENV FLASK_APP=app.py
RUN pip install Flask
RUN pip install forex-python 
RUN  pip install matplotlib
COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
