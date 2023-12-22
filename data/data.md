## Amazon Product Review Data

### Description
The dataset consists of reviews from various Amazon product categories from [Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html). The reviews are categorized into individual datasets based on the product categories they fall in. We will be using the "smaller" datasets provided by the repository in our experimentation. The smaller datasets were produced by extracting the 5-core of the dataset. This essentially results in each user and product having at most 5 reviews each.

### Data Format
Our data is stored in csv format where each line is a product review. Each review has fields for `overall` rating, `verified`, `reviewTime`, `reviewerID`, `asin`, `reviewerName`, `reviewText`, `summary`, and `unixReviewTime`.

Here's an example for a review entry:
```json
{
    "overall": 5.0,
    "verified": true,
    "reviewTime": "11 14, 2013",
    "reviewerID": "A3H7T87S984REU",
    "asin": "B0000530HU",
    "reviewerName": "houserules18",
    "reviewText": "Like the oder and the feel when I put it on my face.  I have tried other brands but the reviews from people I know they prefer the oder of this brand. Not hard on the face when dry.  Does not leave dry skin.",
    "summary": "Good for the face",
    "unixReviewTime": 1384387200
}
```

### Dataset Collection
We source all of our data from [Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html). We plan to incorporate a variety of these product categories in our dataset. We chose to include all the categories in our final dataset. The categories are as follows:
```
["AMAZON FASHION",
"All Beauty",
"Appliances",
"Arts, Crafts and Sewing",
"Automotive",
"Books",
"CDs and Vinyl",
"Cell Phones and Accessories",
"Clothing, Shoes and Jewelry",
"Digital Music",
"Electronics",
"Gift Cards",
"Grocery and Gourmet Food",
"Home and Kitchen",
"Industrial and Scientific",
"Kindle Store",
"Luxury Beauty",
"Magazine Subscriptions",
"Movies and TV",
"Musical Instruments",
"Office Products",
"Patio, Lawn and Garden",
"Pet Supplies",
"Prime Pantry",
"Software",
"Sports and Outdoors",
"Tools and Home Improvement",
"Toys and Games",
"Video Games"]
```
We have performed the following steps to clean our data
1. Read in the first 50,000 reviews from each product category
2. Remove the `vote`, `image`, `style` columns since they have a lot of null entries
3. Remove any null summary or null reviewText entries
4. Remove duplicate summaries
4. Sample 500 reviews from each product category
5. Perform training/dev/test split on each product category to be sized 80%/10%/10%
6. Concatenate all of the respective training/dev/test sets together
    - Final Training Dataset size: 11,095 rows
    - Final Validation Dataset size: 1,387 rows
    - Final Testing Dataset size: 1,388 rows

### Links
- [Original Datasets](https://nijianmo.github.io/amazon/index.html)
- [Training/Validation/Testing Datasets](https://drive.google.com/drive/folders/1NFx5DrLyrWTPCm-Yu0XX3tF_t_0HZw17?usp=sharing)

