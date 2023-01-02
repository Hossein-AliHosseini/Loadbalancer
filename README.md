# Loadbalancer

Simple implementation of a Loadbalancer which listens on port 80 (actually not listening, it is just port forwarding :))


## Run Locally

Clone the project

```bash
  git clone https://github.com/Hossein-AliHosseini/Loadbalancer.git
```

Apply iptables rules

```bash
  sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
  sudo iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
```

Create virtualenv

```bash
  virtualenv venv
  source venv/bin/activate
```

Run Backend containers

```bash
  docker-compose up -d
```

Run Loadbalancer

```bash
  python loadbalancer.py
```

Now open your browser and send request to localhost port 80 :)