# Template

_Update: Feb 23 transferred files from [Risk and Reliability Book](https://gitlab.tudelft.nl/interactivetextbooks-citg/risk-and-reliability/) to set things up._

This will be the future home of the template book. Design philosophy:
- people will fork this to create a book in as easy-as-possible a way
- minimal changes should be made to the book contents itself, to prevent downstream merge conflicts
- focus is mostly on providing a clean and simply view to the key features in our book repo (e.g., config files, scripts, markup flags, etc)

# How to deploy a fork of this book on GitHub Pages

1. Click `Fork`, and set a name for your new book.
2. To enable deploying via GitHub Actions, go to `⚙ Settings`, then to `Pages`, and under `Build and Deployment` set `Source` to `GitHub Actions`.
3. To trigger a deployment for the first time, you can go to `Actions` (top panel), then click `deploy-book` on the left, then `Run workflow` on the right. The book is also automatically deployed whenever commits are pushed onto the `main` branch of the repository (in absence of errors).

Voila! You can now access the copy of the template at 
`https://<username>.github.io/<bookname>` (e.g. `https://psor-books.github.io/template`).

To learn more about how we do this, please see the [GitHub Actions documentation](https://docs.github.com/en/actions) and our deployment pipeline configuration file `.github/workflows/deploy-book-ghpages.yml`.