docker run --rm  --name="student1" --network my_network  student
docker run --rm  --name="student2" --network my_network student
docker run --rm --name nginx -p 8000:80 -v ./nginx.conf:/etc/nginx/nginx.conf --network my_network nginx