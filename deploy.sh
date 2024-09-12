sudo docker-compose down -v
sudo docker rm -f $(sudo docker ps -a -q)
sudo docker system prune -a -f
sudo docker-compose -f docker-compose.yml up --build -d
