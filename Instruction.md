# ENV
```
conda create -n transformer python==3.8

# install requirements
pip install -r requirements.txt

# install custom packages
pip install pkgs/de_core_news_sm-3.7.0-py3-none-any.whl
pip install pkgs/en_core_web_sm-3.3.0-py3-none-any.whl

```
## Modify official code
update util/tokenizer.py  
```
# self.spacy_de = spacy.load('de_core_news_sm')
# self.spacy_en = spacy.load('en_core_web_sm')

# ->

import en_core_web_sm
import de_core_news_sm

self.spacy_de = de_core_news_sm.load()
self.spacy_en = en_core_web_sm.load()

```

util/data_loader.py
```
# from torchtext.legacy.data import Field, BucketIterator
# from torchtext.legacy.datasets.translation import Multi30k

from torchtext.data import Field, BucketIterator
from torchtext.datasets.translation import Multi30k

```

# Prepare train/val dataset
I have downloaded [multi30k](https://github.com/multi30k/dataset) and unziped & moved on .data/multi30k, you can run `python train.py` for training directly.