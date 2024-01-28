# Web Infrastructure Design Project

## Introduction

Hello! I am Redouane Drihmia, a student working on the Web Infrastructure Design project. In this project, I've explored various concepts such as DNS, monitoring, web servers, network basics, load balancers, and servers. The goal is to design and understand web infrastructures, keeping in mind aspects like redundancy, security, and scalability.

## Learning Objectives

By completing this project, I have achieved the following learning objectives:

- Drawing comprehensive diagrams covering the web stack with a focus on components and their roles.
- Explaining the purpose of each component, understanding system redundancy, and becoming familiar with acronyms like LAMP, SPOF, and QPS.

## Project Files

1. [Simple Web Stack Diagram](./0-simple_web_stack)
   - Task 0: A one-server web infrastructure hosting www.foobar.com.
   - Components: 1 Server, 1 Web Server (Nginx), 1 Application Server, 1 Application Files (Code Base), 1 Database (MySQL).

2. [Distributed Web Infrastructure Diagram](./1-distributed_web_infrastructure)
   - Task 1: A three-server setup hosting www.foobar.com with load balancing.
   - Components: 2 Servers, 1 Web Server (Nginx), 1 Application Server, 1 Load Balancer (HAproxy), 1 Application Files, 1 Database (MySQL).

3. [Secured and Monitored Web Infrastructure Diagram](./2-secured_and_monitored_web_infrastructure)
   - Task 2: Enhanced security and monitoring for www.foobar.com.
   - Components: 3 Firewalls, 1 SSL Certificate for HTTPS, 3 Monitoring Clients.

4. [Scaling Up Diagram](./3-scale_up)
   - Task 3: An advanced setup with component separation and load balancer cluster.
   - Components: 1 Server, 1 Load-Balancer (HAproxy) configured as a cluster, individual servers for Web, Application, and Database.

---

Feel free to explore each diagram for an in-depth view of the evolving web infrastructure.

