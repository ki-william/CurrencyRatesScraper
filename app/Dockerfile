FROM python
WORKDIR /app
COPY app.py /app
COPY config.py /app
COPY requirments.txt /app
RUN pip install -r requirments.txt
CMD python app.py