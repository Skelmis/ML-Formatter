ML Formatter
------------

A simple set of scripts that take act as a middle man for media 
intake during  machine learning pipelines. 

Given input arguments, this program aims to produce
the required output format for specific use cases. 

Currently:
 - DeepSpeech

### Usage

```shell
> python -m formatter
```

To view all arguments
```shell
> python -m formatter --help
```

TODO:
 - [x] Add argument parsing
 - [x] Argument validation
 - [ ] Define DeepSpeech formatter
   - [x] Handle empty media dirs
   - [x] Handle media not having transcripts (Warn)
   - [x] Handle non-empty output dirs
   - [ ] Add usage in __main__.py
 - [ ] Fuzzy transcript matching
 - [x] Add __main__.py as a possible program entry point
   - [ ] Full CLI support
     - [ ] Support train/test/dev split