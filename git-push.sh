git add .

echo "Files has been staged"

read -p "Enter commit message : " commitMessage

git commit -m "$commitMessage"

echo "Files has been committed"

echo "Pushing..."

git push

echo "Files has been pushed to your repository"
