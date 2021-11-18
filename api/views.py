#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import re
from flask import request, jsonify
from .util import auto_summarise


def process_summary():
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