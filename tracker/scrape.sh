#!/bin/bash


# Colours to highlight script output.
NC='\033[0m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
GREEN='\033[0;32m'
RED='\033[0;31m'

# Find the root of the repo (must be somewhere inside repo for this to work)
root=$(git rev-parse --show-toplevel)
work_dir=$root/FashionScrapy

###################################################################################################
###################################################################################################


# Website targets currently being used.
targets=( amazon )


###################################################################################################
###################################################################################################


## 
# Function to clean the logs and output directories
# populated by scrapy.
function clean_directories {
    echo -e ${CYAN}Cleaning logs and output directories $i ${NC}
    if [ -d "$work_dir/logs/" ]; then rm -Rf $work_dir/logs/; fi
    if [ -d "$work_dir/output/" ]; then rm -Rf $work_dir/output/; fi
    return
}

##
# Clean the __pycache__ folders.
function pyclean () {
    echo -e ${CYAN}Cleaning python cache files$i ${NC}
    find $root -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
}

##
# Detect errors in output logs.
# @param: parsing target
function errorDetect() {
    if [ -z "$1" ]; then
        echo -e ${RED} Error detection not active$i ${NC}
        exit 0
    fi

    if grep -q "ERROR" $work_dir/logs/$1.log; then
        echo -e ${RED} Error detected parsing $i ${NC}
    fi
}


##
# Run spiders and output logs, images, and json.
function run() {
    # Need to make sure the logs and output directories exist.
    mkdir -p $work_dir/logs
    mkdir -p $work_dir/output
    cd $work_dir 2>&1

    # Iterate through targets and scrape websites.
    for i in "${targets[@]}"
    do
        echo -e ${CYAN}FashionScrapy: scraping $i ${NC}
        # Crawl targets, output as json, and log the output.
        scrapy crawl $i -o $work_dir/output/$i.json --logfile $work_dir/logs/${i}.log
        errorDetect $i
    done
}

##
# Prints commands to set up environment for user
function env() {
    cd $root
    echo -e ${CYAN}python3 -m venv env ${NC}
    echo -e ${CYAN}source env/bin/activate ${NC}
    echo -e ${CYAN}pip3 install -r $root/requirements.txt ${NC}
}

##
# Help menu
function help() {
    # Display Help
    echo -e ${CYAN}"This script will be used to help clean and run the spiders." ${NC}
    echo -e ${CYAN}"It can also help to create compressed log files " ${NC}
    echo
    echo -e ${GREEN}"Syntax: ./scrapy.sh [ env | clean | debug | run | pr | pr-all | rebuild ]" ${NC}
    echo -e ${MAGENTA} "options:" ${NC}
    echo -e ${MAGENTA} "env           Outlines how to setup environment." ${NC}
    echo -e ${MAGENTA} "clean         Cleans output directories and all python caches in repo." ${NC}
    echo -e ${MAGENTA} "run           Runs spiders on all specified targets." ${NC}
    echo
}


###################################################################################################
###################################################################################################

if [[ $1 == "env" ]]; then
    env

elif [[ $1 == "clean" ]]; then
    clean_directories
    pyclean

elif [[ $1 == "debug" ]]; then
    clean_directories
    debug

elif [[ $1 == "run" ]]; then
    clean_directories
    run

elif [[ $1 == "pr" ]]; then
    clean_directories
    pyclean
    pull_request

elif [[ $1 == "pr-all" ]]; then
    clean_directories
    pyclean
    pull_request_all

elif [[ $1 == "rebuild" ]]; then
    clean_directories
    pyclean
    run

else
    help
fi

exit 0
