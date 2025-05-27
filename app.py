from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from main import agent_with

load_dotenv()
