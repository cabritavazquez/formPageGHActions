BUCKETS_FOLDERS=$(jq -r '.Environment.DEV | map(.Bucket_name + " " + .Folder) | @tsv' configuration.json)

# Iterar sobre los nombres de los buckets y las carpetas
for row in $BUCKETS_FOLDERS; do
  # Separar el nombre del bucket y el nombre de la carpeta
  BUCKET_NAME=$(echo "$row" | cut -f1)