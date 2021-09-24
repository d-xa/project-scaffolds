FROM python:3

COPY requirements.txt .

# pip install & update
RUN pip install --upgrade pip && pip install -r requirements.txt

# install spark 3.1.1
RUN apt update \
    && apt -y install default-jre \
    && curl -O https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz \
    && tar xvf spark-3.1.1-bin-hadoop3.2.tgz \
    && mv spark-3.1.1-bin-hadoop3.2/ /opt/spark \
    && echo 'export SPARK_HOME=/opt/spark' | tee -a ~/.bashrc \
    && echo 'export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin' | tee -a ~/.bashrc
