echo "Imagens disponíveis:"
docker images

aws lightsail push-container-image --region us-east-1 --service-name socialnetworkpy --label socialnetworkpy --image socialnetworkpy:latest