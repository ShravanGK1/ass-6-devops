@echo off
title Jenkins Server
echo Starting Jenkins Server on http://localhost:8080 ...
"C:\Program Files\Java\jdk-24\bin\java.exe" -jar "C:\Users\Shravan Joshi\jenkins.war" --enable-future-java --httpPort=8080
pause


