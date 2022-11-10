# mapreduce
Git repository for ICS map-reduce practice

Author: David Fraga Rodríguez
Email: david.fraga.rodriguez@udc.es

## Ejecución

### temperatura_max_min

```bash
docker run --hostname=quickstart.cloudera --privileged=true -t -i --cpus=4 -v $HOME/Desktop/college/ICS/Prácticas/MapReduce/mapreduce/mapreduce/temperatura_max_min:/home/cloudera/practicas --publish-all=true -p 7180 cloudera/quickstart /usr/bin/docker-quickstart

cd /home/cloudera/practicas
hdfs dfs -put files/2017/
hdfs dfs -ls

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.reduces=2 -input 2017 -output salida_2017 -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

hdfs dfs -ls salida_2017
hdfs dfs -cat salida_2017/part-00000 | sort -k 2 -n
hdfs dfs -cat salida_2017/part-00001 | sort -k 2 -n
hdfs dfs -get salida_2017
exit

python3 obtain_result_from_reducer.py
```

### webclient_logs

```bash
docker run --hostname=quickstart.cloudera --privileged=true -t -i --cpus=4 -v $HOME/Desktop/college/ICS/Prácticas/MapReduce/mapreduce/mapreduce/webclient_logs:/home/cloudera/practicas --publish-all=true -p 7180 cloudera/quickstart /usr/bin/docker-quickstart

cd /home/cloudera/practicas
hdfs dfs -put files/condensed/272/Feb95/
hdfs dfs -ls

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -input Feb95 -output salida_Feb95 -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

hdfs dfs -ls salida_Feb95
hdfs dfs -cat salida_Feb95/part-00000 | sort -k 2 -n
hdfs dfs -get salida_Feb95/
```

### wine_quality

```bash
docker run --hostname=quickstart.cloudera --privileged=true -t -i --cpus=4 -v $HOME/Desktop/college/ICS/Prácticas/MapReduce/mapreduce/mapreduce/wine_quality/:/home/cloudera/practicas --publish-all=true -p 7180 cloudera/quickstart /usr/bin/docker-quickstart

cd /home/cloudera/practicas
hdfs dfs -put files/
hdfs dfs -ls

/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -input files/ -output salida_wines -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

hdfs dfs -ls salida_wines
hdfs dfs -cat salida_wines/part-00000 | sort -k 2 -n
hdfs dfs -get salida_wines/
```