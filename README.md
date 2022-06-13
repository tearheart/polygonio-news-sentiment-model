# PolygonIO News Sentiment - Model

This README is for the sentiment analysis model.

# Data
[Polygon.io Ticker News](https://polygon.io/docs/stocks/get_v2_reference_news)

`GET /v2/reference/news`

**Get the most recent news articles relating to a stock ticker symbol, including a summary of the article and a link to the original source.**

**Parameters**
`ticker` Return results that contain this ticker.
`published_utc` Return results published on, before, or after this date.
`order` Order results based on the `sort` field.
`limit` Limit the number of results returned, default is 10 and max is 1000.
`sort` Sort field used for ordering.

**Response Attributes**
`count` [integer] The total number of results for this request.
`next_url` [string] If present, this value can be used to fetch the next page of data.
`request_id` [string] A request id assigned by the server.
`results` [array]
- `amp_url` [string] The mobile friendly Accelerated Mobile Page (AMP) URL.
- `article_url` [string] A link to the news article.
- `author` [string] The article's author.
- `description` [string] A description of the article.
- `id` [string] Unique identifier for the article.
- `image_url` [string] the article's image URL.
- `keywords` [array [string]] The keywords associated with the article (which will vary depending on the publishing source).
- `published_utc` [string] The date the article was published on.
- `publisher` [object]
    - `favicon_url` [string] The publisher's homepage favicon URL.
    - `homepage_url` [string] The publisher's homepage URL.
    - `logo_url` [string] The publisher's logo URL.
    - `name` [string] The publisher's name.
- `tickers` [array [string]] The ticker symbols associated with the article.
- `title` [string] The title of the news article.
- `status` [string] The status of this request's response.

**Response Object Example**
`
{
 "count": 1,
 "next_url": "https://api.polygon.io:443/v2/reference/news?cursor=eyJsaW1pdCI6MSwic29ydCI6InB1Ymxpc2hlZF91dGMiLCJvcmRlciI6ImFzY2VuZGluZyIsInRpY2tlciI6e30sInB1Ymxpc2hlZF91dGMiOnsiZ3RlIjoiMjAyMS0wNC0yNiJ9LCJzZWFyY2hfYWZ0ZXIiOlsxNjE5NDA0Mzk3MDAwLG51bGxdfQ",
 "request_id": "831afdb0b8078549fed053476984947a",
 "results": [
  {
   "amp_url": "https://amp.benzinga.com/amp/content/20784086",
   "article_url": "https://www.benzinga.com/markets/cryptocurrency/21/04/20784086/cathie-wood-adds-more-coinbase-skillz-trims-square",
   "author": "Rachit Vats",
   "description": "<p>Cathie Wood-led Ark Investment Management on Friday snapped up another 221,167 shares of the cryptocurrency exchange <strong>Coinbase Global Inc </strong>(NASDAQ: <a class=\"ticker\" href=\"https://www.benzinga.com/stock/coin#NASDAQ\">COIN</a>) worth about $64.49 million on the stock&rsquo;s Friday&rsquo;s dip and also its fourth-straight loss.</p>\n<p>The investment firm&rsquo;s <strong>Ark Innovation ETF</strong> (NYSE: <a class=\"ticker\" href=\"https://www.benzinga.com/stock/arkk#NYSE\">ARKK</a>) bought the shares of the company that closed 0.63% lower at $291.60 on Friday, giving the cryptocurrency exchange a market cap of $58.09 billion. Coinbase&rsquo;s market cap has dropped from $85.8 billion on its blockbuster listing earlier this month.</p>\n<p>The New York-based company also added another 3,873 shares of the mobile gaming company <strong>Skillz Inc</strong> (NYSE: <a class=\"ticker\" href=\"https://www.benzinga.com/stock/sklz#NYSE\">SKLZ</a>), <a href=\"http://www.benzinga.com/markets/cryptocurrency/21/04/20762794/cathie-woods-ark-loads-up-another-1-2-million-shares-in-skillz-also-adds-coinbase-draftkin\">just a day after</a> snapping 1.2 million shares of the stock.</p>\n<p>ARKK bought the shares of the company which closed ...</p><p><a href=https://www.benzinga.com/markets/cryptocurrency/21/04/20784086/cathie-wood-adds-more-coinbase-skillz-trims-square alt=Cathie Wood Adds More Coinbase, Skillz, Trims Square>Full story available on Benzinga.com</a></p>",
   "id": "nJsSJJdwViHZcw5367rZi7_qkXLfMzacXBfpv-vD9UA",
   "image_url": "https://cdn2.benzinga.com/files/imagecache/og_image_social_share_1200x630/images/story/2012/andre-francois-mckenzie-auhr4gcqcce-unsplash.jpg?width=720",
   "keywords": [
    "Sector ETFs",
    "Penny Stocks",
    "Cryptocurrency",
    "Small Cap",
    "Markets",
    "Trading Ideas",
    "ETFs"
   ],
   "published_utc": "2021-04-26T02:33:17Z",
   "publisher": {
    "favicon_url": "https://s3.polygon.io/public/public/assets/news/favicons/benzinga.ico",
    "homepage_url": "https://www.benzinga.com/",
    "logo_url": "https://s3.polygon.io/public/public/assets/news/logos/benzinga.svg",
    "name": "Benzinga"
   },
   "tickers": [
    "DOCU",
    "DDD",
    "NIU",
    "ARKF",
    "NVDA",
    "SKLZ",
    "PCAR",
    "MASS",
    "PSTI",
    "SPFR",
    "TREE",
    "PHR",
    "IRDM",
    "BEAM",
    "ARKW",
    "ARKK",
    "ARKG",
    "PSTG",
    "SQ",
    "IONS",
    "SYRS"
   ],
   "title": "Cathie Wood Adds More Coinbase, Skillz, Trims Square"
  }
 ],
 "status": "OK"
}
`

# Model

###FinBERT: Financial Sentiment Analysis with BERT

**"FinBERT is a pre-trained NLP model to analyze sentiment of financial text. It is built by further training the BERT language model in the finance domain, using a large financial corpus and thereby fine-tuning it for financial sentiment classification."**

**FinBERT Paper:** [FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.](https://arxiv.org/pdf/1908.10063.pdf)

**FinBERT Repository:** [ProsusAI/finBERT](https://github.com/ProsusAI/finBERT)
