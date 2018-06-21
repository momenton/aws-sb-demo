FROM python:3

RUN mkdir /code
WORKDIR /code

#If we add the requirements and install dependencies first, docker can use cache if requirements don't change
COPY . /code/
RUN pip install --no-cache-dir -r requirements.txt

CMD python app.py