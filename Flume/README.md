#Flume setup (keep tracking them on 3 different terminals)

Start Listening

•	spark-submit --packages org.apache.spark:spark-streaming-flume_2.11:2.3.0 SparkFlume.py (for HDP 2.6.5)

To start Flume agent,

Go to Flume server dir

•	cd /usr/hdp/current/flume-server/

Start Agent with necessary conf file

•	sudo bin/flume-ng agent --conf conf --conf-file ~/sparkstreamingflume.conf --name a1 -Dflume.root.logger=INFO,console

To read data, copy some files to /spool/ dir

•	cp access_log.txt spool/mylog3.txt
