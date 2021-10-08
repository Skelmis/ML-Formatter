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

Example usage
```shell
> python -m formatter --media ./media --transcript ./transcripts --output ./output --verbose
```

TODO:
 - [x] Add argument parsing
 - [x] Argument validation
 - [x] Define DeepSpeech formatter
   - [x] Handle empty media dirs
   - [x] Handle media not having transcripts (Warn)
   - [x] Handle non-empty output dirs
   - [x] Add usage in __main__.py
   - [x] Actual implementation
     - [x] Process all files
     - [x] Split into train/test/dev splits
     - [x] Shuffle files before performing the split for randomisation 
     - [x] Move files to output dir (Hard linking)
 - [x] Add __main__.py as a possible program entry point
   - [x] Full CLI support
     - [x] Support train/test/dev split