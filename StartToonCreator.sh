#!/bin/bash
cd src
RESOURCES_DIR=$(head -n 1 ../config/RESOURCES_DIR) && python main.py
