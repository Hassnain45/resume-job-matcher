---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:903
- loss:TripletLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: Looking for a candidate with skills and experience in Arts.
  sentences:
  - education details llb dibrugarh university advocate skill details legal exprience
    less than 1 year monthscompany details company legal description advocate
  - education details bachelor s bachelor s commerce india guru nanak high school
    sales manager skill details data entry exprience less than 1 year months cold
    calling exprience less than 1 year months sales exprience less than 1 year months
    salesforce exprience less than 1 year months ms office exprience less than 1 year
    monthscompany details company emperor honda description company honda cars india
    ltd description 1 worked as an asm at maruti dealership for 10 years 2 currently
    working as manager sales in honda car dealership from last 5 years 3 good sportsmen
    represent my college in various cricket tournaments 4 lead nagpur university cricket
    team also 5 searching job in car dealership or cricket academy
  - education details january 2017 rachana sansad school of interior deign january
    2013 holy family high school master of commerce marketing mumbai maharashtra university
    of mumbai drawing arts craft teacher drawing arts craft teacher ghatkopar ymca
    skill details company details company ghatkopar ymca description for 3 years worked
    in jungle cubs gym as a co ordinator for 1 year
- source_sentence: Looking for a candidate with skills and experience in HR.
  sentences:
  - education details mba acn college of engineering mgt hr skill details company
    details company hr assistant description
  - training in special education certificate course education details july 2016 to
    october 2018 m sc psychology with specialization in organizational behaviour malappuram
    kerala calicut university july 2013 to march 2016 bsc psychology thrissur prajyoti
    niketan college hr skill details company details company description i have done
    a 30 days internship in the hr department of foster hot breads kinfra malappuram
    kerala and i have also done a 60 days internship at santhwana institute of counselling
    and psychotherapy cochin kerala as counsellor
  - education details august 2018 to january 2021 entermediate maths mumbai maharashtra
    sunbeam academy samne ghat varanasi martial arts fitness job skill details company
    details company sports authority description i am 2nd dan black belt in karate
    martial arts i am in a searching of personal trainer job for fitness i won 3 gold
    medals in national karate championship i won 7 gold medals in state karate championship
    3 times best player of the year of uttar pradesh award represented india and selected
    for world karate championship held at croatia europe
- source_sentence: Looking for a candidate with skills and experience in Health and
    fitness.
  sentences:
  - education details llb dibrugarh university advocate skill details legal exprience
    less than 1 year monthscompany details company legal description advocate
  - education details january 1992 to january 2003 first year science mumbai maharashtra
    st micheal high personal fitness trainer level3 personal trainer skill details
    company details company golds gym fitness solution flora hotel description certification
    american college of sports science golds gym heart saver reps level 3 responsibilities
    to obtain a challenging position which will commensurate with my qualification
    and experience in the field of health and fitness environment accomplishments
    good skills used fitness
  - computer skills software knowledge ms power point ms office c protius pcb design
    multisim micro wind matlab keil latex basic i nternet fundamentals software and
    hardware knowledge project details diploma project speed control of dc motor using
    heart beats mini project water gardening system using solar panel final year be
    project iris recognition system education details january 2016 be education pune
    maharashtra pune university january 2010 ssc maharashtra board quality engineer
    quality engineer matrix technologies skill details matlab exprience 6 months pcb
    exprience 6 months pcb design exprience 6 monthscompany details company matrix
    technologies description company rb electronics description
- source_sentence: Looking for a candidate with skills and experience in HR.
  sentences:
  - good grasping quality and skillful work education details march 2013 to march
    2018 b a ll b law solapur maharashtra solapur university advocate skill details
    good knowledge of typing as well as many other activities exprience less than
    1 year monthscompany details company district and session court of solapur description
    forward thinking individual with refined interpersonal and multitasking skills
    looking to join a progressive organization to provide assistance in legal work
    company district and session court of solapur description provide legal assistance
    in legal work
  - education details bachelor s bachelor s commerce india guru nanak high school
    sales manager skill details data entry exprience less than 1 year months cold
    calling exprience less than 1 year months sales exprience less than 1 year months
    salesforce exprience less than 1 year months ms office exprience less than 1 year
    monthscompany details company emperor honda description company honda cars india
    ltd description 1 worked as an asm at maruti dealership for 10 years 2 currently
    working as manager sales in honda car dealership from last 5 years 3 good sportsmen
    represent my college in various cricket tournaments 4 lead nagpur university cricket
    team also 5 searching job in car dealership or cricket academy
  - education details june 2012 to may 2015 b a economics chennai tamil nadu sdnbvc
    hr skill details company details company anything it solution description hr
- source_sentence: Looking for a candidate with skills and experience in Advocate.
  sentences:
  - education details august 2010 to may 2017 be electronics communication jabalpur
    madhya pradesh takshshila institute of technology java developer skill details
    java javascript exprience 6 monthscompany details company wab it softwere pvt
    ltd description jr java developer
  - hard working quick learnereducation details june 2014 to may 2017 llb law mumbai
    maharashtra mumbai university january 2014 b com commerce mumbai maharashtra mumbai
    university january 2011 hsc maharashtra board january 2009 ssc maharashtra board
    advocate skill details company details company the vidishtra description
  - education details june 2013 to june 2016 diploma computer science pune maharashtra
    aissms june 2016 be pursuing computer science pune maharashtra anantrao pawar
    college of engineering research centre python developer skill details company
    details company cybage software pvt ltd description i want to work in organisation
    as a python developer to utilize my knowledge to gain more knowledge with our
    organisation
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps inputs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision 1110a243fdf4706b3f48f1d95db1a4f5529b4d41 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'mean', 'include_prompt': True})
  (2): Normalize({'module_input_name': 'sentence_embedding', 'module_output_name': 'sentence_embedding'})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```
Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Looking for a candidate with skills and experience in Advocate.',
    'hard working quick learnereducation details june 2014 to may 2017 llb law mumbai maharashtra mumbai university january 2014 b com commerce mumbai maharashtra mumbai university january 2011 hsc maharashtra board january 2009 ssc maharashtra board advocate skill details company details company the vidishtra description',
    'education details june 2013 to june 2016 diploma computer science pune maharashtra aissms june 2016 be pursuing computer science pune maharashtra anantrao pawar college of engineering research centre python developer skill details company details company cybage software pvt ltd description i want to work in organisation as a python developer to utilize my knowledge to gain more knowledge with our organisation',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.8851, -0.0736],
#         [ 0.8851,  1.0000, -0.0670],
#         [-0.0736, -0.0670,  1.0000]])
```
<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 903 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>sentence_2</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                         | sentence_1                                                                           | sentence_2                                                                           |
  |:---------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type     | string                                                                             | string                                                                               | string                                                                               |
  | modality | text                                                                               | text                                                                                 | text                                                                                 |
  | details  | <ul><li>min: 13 tokens</li><li>mean: 14.01 tokens</li><li>max: 15 tokens</li></ul> | <ul><li>min: 21 tokens</li><li>mean: 212.77 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 29 tokens</li><li>mean: 225.29 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | sentence_0                                                                           | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  |:-------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Looking for a candidate with skills and experience in ETL Developer.</code>    | <code>technicalproficiencies db oracle 11g domains investment banking advertising insurance programming skills sql plsql bi tools informatica 9 1 os windows unix professional development trainings concepts in data warehousing business intelligence etl bi tools informatica 9x education details bca nanded maharashtra nanded university etl developer etl developer sun trust bank ny skill details etl exprience 39 months extract transform and load exprience 39 months informatica exprience 39 months oracle exprience 39 months unix exprience 39 monthscompany details company sun trust bank ny description sun trust bank ny jan 2018 to present client sun trust bank ny environment informatica power center 9 1 oracle 11g unix role etl developer project profile sun trust bank is a us based multinational financial services holding company headquarters in ny that operates the bank in new york and other financial services investments the company is organized as a stock corporation with four divisions investm...</code> | <code>key competencies multi operations management people management customer services emails mis vendor client services management cross functional coordination banking financial services transaction monitoring atm operations prepaid card operations pre issuance post issuance pos operations job profile skills an effective communicator with excellent relationship building interpersonal skills strong analytical problem solving organizational abilities extensive experience in managing operations with demonstrated leadership qualities organisational skills during the tenure managing customer centric operations ensuring customer satisfaction by achieving service quality norms analyzing of all operational problems customer complaints and take preventive and corrective actions to resolve the same receive and respond to key customer inquiries in an effective manner and provide relevant and timely information deft in steering banking back end operations analyzing risks and managing delinquencies wit...</code> |
  | <code>Looking for a candidate with skills and experience in Java Developer.</code>   | <code>education details january 2013 master of engineering information technology pune maharashtra m i t january 2005 bachelor of engineering information technology pusad maharashtra amravati university january 2001 pusad maharashtra p n junior college january 1999 s s c pusad maharashtra k d high school java developer java developer maxgen technologies skill details company details company maxgen technologies description currently working in infrasoft technologies andheri as a java developer company mis generation of tata sky and tata power description courses done android mobile app development technologies in java core java advance java jsf hibernate spring at niit in 2015 16 android project location detector of computing and mobile devices android me project data deduplication my projects works to reduce redundant data from the system and free up the memory it stores unique copy of data and for more location with same data with the help of pointers can access the data java subjects taugh...</code> | <code>education details may 2013 to may 2017 b e uit rgpv data scientist data scientist matelabs skill details python exprience less than 1 year months statsmodels exprience 12 months aws exprience less than 1 year months machine learning exprience less than 1 year months sklearn exprience less than 1 year months scipy exprience less than 1 year months keras exprience less than 1 year monthscompany details company matelabs description ml platform for business professionals dummies and enthusiasts 60 a koramangala 5th block achievements tasks behind sukh sagar bengaluru india developed and deployed auto preprocessing steps of machine learning mainly missing value treatment outlier detection encoding scaling feature selection and dimensionality reduction deployed automated classification and regression model linkedin com in aditya rathore b4600b146 reasearch and deployed the time series forecasting model arima sarimax holt winter and prophet worked on meta feature extracting problem github com...</code> |
  | <code>Looking for a candidate with skills and experience in DotNet Developer.</code> | <code>technical skills category skills language c c oop dot net technologies asp net mvc ado net entity framework linq web technologies html css browser scripting javascript jquery ajax json web browser internet explorer 8 0 mozilla firefox10 front end framework bootstrap kendo ui database sql server 2012 development tools visual studio 2013 operating systems ms window 2007 project details projects worked on 1 project name politician website role trainee project description i developed politician website in this website there is home page quick facts category biography gallery and contactus page it is a totally dynamic website environment operating system windows 7 development tools visual studio 2013 database server sql server 2012 technology net framework 4 5 asp net mvc5 presentation layer html css jquery bootstrap role and responsibilities understanding requirements coding and unit testing 2 project name coaching management system cms project description this software is helps to manage ...</code> | <code>core competencies maintain processes to ensure project management documentation reports and plans are relevant accurate and complete report automation dashboard preparation and sharing feedbacks basis on performance of project manager forecasting data regarding future risks project changes and updating the delivery team on timely basis good understanding of project management lifecycle proven excellence in risk management and control good understanding of software development lifecycle sdlc ability to synthesize qualitative and quantitative data quickly and draw meaningful insights knowledge of programme project management methodologies with full project reporting and governance ability to work with different cross functional stakeholders to establish and ensure a reliable and productive working relationship strong time management and organizational skills multitasking skills and ability to meet deadlines computer skills and certification advance knowledge in ms office 2013 and macros ...</code> |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.EUCLIDEAN",
      "triplet_margin": 5
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 8
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 8
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `dataloader_multiprocessing_context`: None
- `dataloader_in_order`: True
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}
- `warmup_ratio`: None

</details>

### Training Time
- **Training**: 12.2 minutes

### Framework Versions
- Python: 3.13.15
- Sentence Transformers: 6.0.1
- Transformers: 5.17.0
- PyTorch: 2.14.0+cpu
- Accelerate: 1.15.0
- Datasets: 5.0.1
- Tokenizers: 0.23.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### TripletLoss
```bibtex
@misc{hermans2017defense,
    title={In Defense of the Triplet Loss for Person Re-Identification},
    author={Alexander Hermans and Lucas Beyer and Bastian Leibe},
    year={2017},
    eprint={1703.07737},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->