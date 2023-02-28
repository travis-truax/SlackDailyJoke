set -x 
rm daily_smile.zip

mkdir -p payload
cp src/* payload

pip install -r requirements.txt --target payload

cd payload
zip -r daily_smile .
mv daily_smile.zip ..
cd ..

rm -rf payload
