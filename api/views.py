#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify, request
from .util import auto_summarise

def process_summary():
    """
    It takes in a POST request with a JSON body containing the text to be summarized and the number of
    sentences to be returned. It then calls the `auto_summarise` function from the `summarizer` module
    and returns the summary as a JSON response.
    
    :return: a json object with the summary of the text.
    """
    if request.method == 'POST':
        request_dict = request.get_json(force=True)
        try:
            if "text" in request_dict and request_dict["text"]:
                summary = auto_summarise(request_dict["text"], request_dict["num_sentences"]) if request_dict.get("num_sentences", None) else auto_summarise(request_dict["text"])
                
                result = {"data": summary}
                return jsonify(result), 200
            else:
                error_str = "Please input text to summarize"
                return jsonify({"error":error_str}), 400     
        except Exception as e:
            error_str = str(e)
            return jsonify({"error_str": error_str}), 500        