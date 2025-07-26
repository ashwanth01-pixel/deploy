kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml

for ubuntu user{

cat /home/ubuntu/.kube/config | base64 -w 0

}
for root user{

mkdir -p /root/.kube

cp /home/ubuntu/.kube/config /root/.kube/config

chown root:root /root/.kube/config


cat ~/.kube/config | base64 -w 0 

}
