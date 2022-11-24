const puppeteer = require("puppeteer");
const fs = require("fs");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(
    "https://generated.photos/faces/natural/young-adult/black-race/long/male/brown-eyes"
  );
  const features = {
    sex: "male",
    race: "race_black",
    hair_color: "hair_dark",
    hair_length: "hair_length_long",
    eye_color: "brown",
    smiling: false,
  };
  const imageCards = await page.$$(".card-image a img");
  // console.log(await (await imageCards.getProperty("src")).toString());

  const db = await require("./faceDatabase");
  console.log(imageCards.length);
  imageCards.forEach(async (element) => {
    const link = await (await element.getProperty("src")).jsonValue();
    console.log(link);
    db[features["sex"]][link] = features;
    console.log(db);
  });

  // STEP 3: Writing to a file
  // fs.writeFile("users.json", JSON.stringify(users), (err) => {
  //   // Checking for errors
  //   if (err) throw err;

  //   console.log("Done writing"); // Success
  // });
  browser.close();
})();

// STEP 1: Reading JSON file
