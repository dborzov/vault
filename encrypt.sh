cp secrets backups/"backup_$(date +%Y%m%d_%H%M%S)"
openssl des3 -d -in secrets -out ~/upencrypted.txt
subl -w ~/upencrypted.txt
openssl des3 -out secrets -in ~/upencrypted.txt
rm ~/upencrypted.txt