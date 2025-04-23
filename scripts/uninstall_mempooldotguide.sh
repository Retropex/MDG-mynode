#!/bin/bash

source /usr/share/mynode/mynode_device_info.sh
source /usr/share/mynode/mynode_app_versions.sh

echo "==================== UNINSTALLING APP ===================="

cd /mnt/hdd/mynode/mempool
docker-compose rm
rm -rf data
rm -rf mysql/data
cd ~

echo "================== DONE UNINSTALLING APP ================="
