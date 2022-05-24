<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">REST API DJANGO </h3>

  <p align="center">
    Rest api app using DRF
    <br />
    <a href="https://github.com/Lubov93/rest_api_blog"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

It is small test app, written on Django Rest Framework.

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation


1.Clone the repo
   ```sh
   git clone https://github.com/Lubov93/test_project_for_cv.git
   ```
2.Activate virtualenv
   ```sh
   source venv/bin/activate
   ```

3.Install packages
   ```sh
   pip install -r requirements.txt
   ```
4.Makemigartions
   ```JS
   python manage.py makemigrations/migrate
   ```
5.Run server
   ```JS
   python manage.py runserver
   ```

<!-- USAGE EXAMPLES -->
## Usage


1.Create new user in post form
   ```JS
   http://127.0.0.1:8000/api/user/ 
   ```
2.Create new product using POST query
   ```JS
   http://127.0.0.1:8000/api/product/ 
   ```
3.Using GET query get list of all products
   ```JS
   http://127.0.0.1:8000/api/product/ 
   ```
4.Get one product by id (GET query)
   ```JS
   http://127.0.0.1:8000/api/product/{id}/ 
   ```
5.Delete one product by id(DELETE query)
   ```JS
   http://127.0.0.1:8000/api/product/{id}/
   ```
6.Update one product by id(PUT query)
   ```JS
   http://127.0.0.1:8000/api/product/{id}/
   ```
7. Using Postman add new images to one or more products
![](https://github.com/Lubov93/test_project_for_cv/images/img.png)

<!-- CONTACT -->
## Contact

My linkendin -  https://www.linkedin.com/in/liubovrudn/
</br>
My email - lubaandpython@gmail.com</br>










