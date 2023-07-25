# Active learning: Working through a JSON example
So, let's work through an example to show how we could make use of some JSON formatted data on a website.

## Getting started
To begin with, make local copies of our [heroes.html](./heroes.html) and [style.css](./style.css) files. The latter contains some simple CSS to style our page, while the former contains some very simple body HTML, plus a `<script>` element to contain the JavaScript code we will be writing in this exercise:
```
<header>
...
</header>

<section>
...
</section>

<script>
...
</script>
```

We have made our JSON data available on our GitHub, at https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json.

We are going to load the JSON into our script, and use some nifty DOM manipulation to display it, like this:

![Screenshot from 2023-07-25 10-04-28](https://github.com/samuelselasi/alx-higher_level_programming/assets/85158665/d6973598-00d8-404b-a4ba-51fcaea457c7)

# Top-level function
The top-level function looks like this:

```
async function populate() {
  const requestURL =
    "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
  const request = new Request(requestURL);

  const response = await fetch(request);
  const superHeroes = await response.json();

  populateHeader(superHeroes);
  populateHeroes(superHeroes);
}

```

To obtain the JSON, we use an API called Fetch. This API allows us to make network requests to retrieve resources from a server via JavaScript (e.g. images, text, JSON, even HTML snippets), meaning that we can update small sections of content without having to reload the entire page.

In our function, the first four lines use the Fetch API to fetch the JSON from the server:

* we declare the requestURL variable to store the GitHub URL
* we use the URL to initialize a new Request object.
* we make the network request using the fetch() function, and this returns a Response object
* we retrieve the response as JSON using the json() function of the Response object.

# Populating the header
Now that we've retrieved the JSON data and converted it into a JavaScript object, let's make use of it by writing the two functions we referenced above. First of all, add the following function definition below the previous code:

```
function populateHeader(obj) {
  const header = document.querySelector("header");
  const myH1 = document.createElement("h1");
  myH1.textContent = obj.squadName;
  header.appendChild(myH1);

  const myPara = document.createElement("p");
  myPara.textContent = `Hometown: ${obj.homeTown} // Formed: ${obj.formed}`;
  header.appendChild(myPara);
}

```

Here we first create an h1 element with createElement(), set its textContent to equal the squadName property of the object, then append it to the header using appendChild(). We then do a very similar operation with a paragraph: create it, set its text content and append it to the header. The only difference is that its text is set to a template literal containing both the homeTown and formed properties of the object.


# Creating the hero information cards
Next, add the following function at the bottom of the code, which creates and displays the superhero cards:

```
function populateHeroes(obj) {
  const section = document.querySelector("section");
  const heroes = obj.members;

  for (const hero of heroes) {
    const myArticle = document.createElement("article");
    const myH2 = document.createElement("h2");
    const myPara1 = document.createElement("p");
    const myPara2 = document.createElement("p");
    const myPara3 = document.createElement("p");
    const myList = document.createElement("ul");

    myH2.textContent = hero.name;
    myPara1.textContent = `Secret identity: ${hero.secretIdentity}`;
    myPara2.textContent = `Age: ${hero.age}`;
    myPara3.textContent = "Superpowers:";

    const superPowers = hero.powers;
    for (const power of superPowers) {
      const listItem = document.createElement("li");
      listItem.textContent = power;
      myList.appendChild(listItem);
    }

    myArticle.appendChild(myH2);
    myArticle.appendChild(myPara1);
    myArticle.appendChild(myPara2);
    myArticle.appendChild(myPara3);
    myArticle.appendChild(myList);

    section.appendChild(myArticle);
  }
}

```

To start with, we store the members property of the JavaScript object in a new variable. This array contains multiple objects that contain the information for each hero.

Next, we use a for...of loop to loop through each object in the array. For each one, we:

1. Create several new elements: an `<article>`, an `<h2>`, three `<p>`s, and a `<ul>`.
2. Set the `<h2>` to contain the current hero's name.
3. Fill the three paragraphs with their secretIdentity, age, and a line saying "Superpowers:" to introduce the information in the list.
4. Store the powers property in another new constant called superPowers — this contains an array that lists the current hero's superpowers.
5. Use another for...of loop to loop through the current hero's superpowers — for each one we create an `<li>` element, put the superpower inside it, then put the listItem inside the `<ul>` element (myList) using appendChild().
6. The very last thing we do is to append the `<h2>`, `<p>`s, and `<ul>` inside the `<article>` (myArticle), then append the `<article>` inside the `<section>`. The order in which things are appended is important, as this is the order they will be displayed inside the HTML.


# Calling the top-level function
Finally, we need to call our top-level populate() function:

```
populate();

```
