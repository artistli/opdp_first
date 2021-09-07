
FROM python:3.7.7-slim

COPY opdp_first ./opdp_first
RUN pip install --no-cache-dir -r opdp_first/requirements.txt


COPY opdp_first /opt/opdp_first/

EXPOSE 9908
WORKDIR /opt/opdp_first

CMD ["python", "main.py", "9908"]
