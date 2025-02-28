# highfiveapp
High Five App

# how it works
Send a high five will send a payload to a logstash port which will then forward that to ES.
A Datasource for ES sits in Grafana.
Dashboard built on the ES DS and then reloads on the main page.

# Requires.
Logstash pipeline that will listen on port: 5099
Elasticsearch that Logstash can send to
Grafana with anonymous login enabled.
