
FROM python:3.9

WORKDIR /app

COPY ./requirements_streamlit_app.txt /app/requirements_streamlit_app.txt

COPY ./img/churn-image.jpeg /app/img/churn-image.jpeg

COPY ./streamlit_app.py /app/streamlit_app.py

RUN pip3 install -r requirements_streamlit_app.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]