<p align="center">
  <a href="" rel="noopener">
    <img width=130px height=60px src="https://www.alfredapp.com/favicon.ico" alt="Project logo">
  </a>
</p>

<p align="center">
  <a href="" rel="noopener">
 <img width=100px height=100px src="https://imgur.com/favicon.ico" alt="Project logo"></a>
</p>

<h3 align="center">alfred-imgur</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-dft)]()
[![GitHub Issues](https://img.shields.io/github/issues/s3cret/Project-Name)](https://github.com/s3cret/alfred-imgur/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/s3cret/Project-Name)](https://github.com/s3cret/alfred-imgur/pulls)
[![License](https://img.shields.io/github/license/s3cret/py-basic)](/LICENSE)

</div>

---

<p align="center">
    Quickly upload image to Imugr using Alfred Workflow.
    <br> 
</p>

## Table of Contents

- [About](#about)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [Upcomming](#upcomming)
- [Contributing](../CONTRIBUTING.md)

## About

Upload last copied image to Imugr using Alfred Workflow.  
**From:**
 - Last Screenshot
 - Clipboard
 - URL

### Motivation

- [ ] To do.

## Getting Started

You need to add your personal information into **two** files:

- `setup.py`
- `modules/api/album_id.py`

Follow the step to generate your `key.json` file under `key/`

1. Replace with your informations in file `setup.py`.

    ```json
    # setup.py
    ...
    {
        "username": "your_username",
        "client_id": "your_client_id",
        "client_secret": "your_client_secret",
        "access_token": "your_access_token",
        "refresh_token": "your_refresh_token",
        "account_id": "your_account_id"
    }
    ...
    ```

2. Then your `album_id.py` file under `modules/api` should look like this:
    ```
    # album_id.py
    # replace your album_id

    your_album_name1 = "your_album_id"

    your_album_name2 = "your_album_id"

    your_album_name3 = "your_album_id"

    ```
- Finally, choose your album in `main.py` file, the `config` variable.
- :tada: Done.


### Requirements

- Python 3 with the following

  ```
  pip install requests
  pip install pasteboard
  pip install imgurpython
  ```

- [pngpaste](https://github.com/jcsalterego/pngpaste):

  ```
  # for mac user:
  brew install pngpaste
  ```

## How to use
- [ ] To do.


## Upcomming

#### In Porgress:  
  - [ ] To use the client from a strictly anonymous context. [imgur/imgurpython](https://github.com/Imgur/imgurpython)


#### Completed
- [x] upload image from **`Clipboard URL`**
- [x] upload image from **`Clipboard File`**
- [x] upload image from latest **`Screenshot`**
- [ ] :bulb: And your ideas:
  - [ ] Eureka
  - [ ] ...

## Contributing

1. Fork it
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request


## Reference
#### From the [Imgur Documentation](https://apidocs.imgur.com/#a94d108b-d6e3-4e68-9521-47ea79501c85):

>- Registration gives you your **`client_id`** and **`client_secret`**, which is then used to authorize the user to your app.  
>
>- Authorization is the process of the user saying  
_"I would like YourSuperAwesomeImgurApp to access my data"_.  
YourSuperAwesomeImgurApp cannot access the user's account without them agreeing to it.  
After they agree, you will get refresh and access tokens.
>
>   - **`access_token`:** is your secret key used to access the user's data.  
>    It can be thought of the user's password and username combined into one, and is used to access the user's account. It expires after 1 month.  
>    - **`refresh_token`**: is used to request new access_tokens. Since access_tokens expire after 1 month, we need a way to request new ones without going through the entire authorization step again. It does not expire.  
>    - **`authorization_code`**: is used for obtaining the the access and refresh tokens. It's purpose is to be immediately exchanged for an access_token and refresh_token.  
>    - Finally, after obtaining your access_token, you make your API requests by sending the Authorization header as such:  
:heavy_check_mark: ```Authorization: Bearer YOUR_ACCESS_TOKEN```  
> - Registration  
Each client must register their application and receive the client_id and client_secret.
For public read-only and anonymous resources, such as getting image info, looking up user comments, etc. all you need to do is send an authorization header with your client_id in your requests. This also works if you'd like to upload images anonymously (without the image being tied to an account), or if you'd like to create an anonymous album. This lets us know which application is accessing the API.  
>
>```Authorization: Client-ID YOUR_CLIENT_ID```

#### **In short:**  
>To create your own `ACCESS_TOKEN` and use it.


