# Scrape public comments from FCC ECFS

Scrape Federal Communications Commssion (FCC) Electronic Comments Filing System (ECFS) via [https://publicapi.fcc.gov/ecfs/filings](https://publicapi.fcc.gov/ecfs/filings).

**Note**: You will require a `data.gov` API key to use this script.  You can sign up for a key at [https://api.data.gov/signup](https://api.data.gov/signup).

## Install

1. Setup a `virtualenv`:

		$ python3 $(which virtualenv) .

2. Activate the `virtualenv`:

	    $ source bin/activate

3. Install requirements:

	    (scrape_fcc_ecfs) $ pip3 install -r requirements.txt

## Usage

    $ ./scrape_fcc_ecfs.py -h
    usage: scrape_fcc_ecfs.py [-h] -p PROCEEDINGS_NAME [-k API_KEY] [-l LIMIT]
                              [-m MAX_OFFSET]

    Scrape Federal Communications Commssion (FCC) Electronic Comments Filing
    System (ECFS) via publicapi.fcc.gov

    optional arguments:
      -h, --help            show this help message and exit
      -p PROCEEDINGS_NAME, --proceedings-name PROCEEDINGS_NAME
                            Proceedings docket ID (e.g., "17-108") (default: None)
      -k API_KEY, --api-key API_KEY
                            data.gov public API key (you can request a key from
                            https://api.data.gov/signup if you don't have one
                            already; also you can set a DATA_DOT_GOV_API_KEY
                            environment variable to avoid entering your key)
                            (default: None)
      -l LIMIT, --limit LIMIT
                            The number of filings to get per request (max=10000)
                            (default: 25)
      -m MAX_OFFSET, --max-offset MAX_OFFSET
                            The maximum offset (should be a multiple of --limit)
                            (default: 25)

## Example

    $ ./scrape_fcc_ecfs.py -p 17-108 -l 1 -m 1 | jq .
    {
      "confirmation_number": "20170427165805575",
      "submissiontype": {
        "description": "COMMENT",
        "short": "COMMENT",
        "id": 7,
        "abbreviation": "CO"
      },
      "attachments": [],
      "documents": [],
      "bureaus": [],
      "id_submission": "10427231705088",
      "lawfirms": [],
      "viewingstatus": {
        "description": "Unrestricted",
        "id": "10"
      },
      "contact_email": "bernardodsanderson@gmail.com",
      "express_comment": 1,
      "addressentity": {
        "city": "Moorhead",
        "address_line_1": "1516 10th Ave N",
        "state": "MN",
        "zip_code": "56560"
      },
      "internationaladdressentity": {
        "addresstext": ""
      },
      "filers": [
        {
          "name": "Bernardo Anderson"
        }
      ],
      "date_submission": "2017-04-27T20:00:05.188Z",
      "date_disseminated": "2017-04-28T15:01:17.543Z",
      "filingstatus": {
        "description": "DISSEMINATED",
        "id": 30
      },
      "proceedings": [
        {
          "sunshine_start_date": null,
          "comment_reply_end_date": null,
          "_index": "proceedings.new",
          "city": " ",
          "date_initial_decision": null,
          "date_nprm": null,
          "id_bureau": " ",
          "id_proceeding": "301759",
          "flag_rulemaking_or_docket": "D",
          "channel": " ",
          "description": "Restoring Internet Freedom",
          "file_number": "",
          "total": 3,
          "date_closed": "2099-12-31T23:59:59.999Z",
          "date_designated": null,
          "date_proceeding_created": "2017-04-26T14:49:35.900Z",
          "callsign": " ",
          "flag_internet_file": "Y",
          "bureau": {
            "code": "WC",
            "name": "Wireline Competition Bureau",
            "edocs_bureau_code": "WCB"
          },
          "id_state": null,
          "sunshine_end_date": null,
          "filed_by": "Aleta.Bowers",
          "date_archived": null,
          "face_card_id": "301759",
          "flag_historical_data_exists": "N",
          "consolidated_proceeding_id": null,
          "date_public_notice": null,
          "date_rule_board_decision": null,
          "flag_archived": "N",
          "flag_small_business_impact": null,
          "description_display": "Restoring Internet Freedom",
          "comment_end_date": null,
          "applicant_name": " ",
          "date_effective": null,
          "comment_start_date": null,
          "filingStatus": "OPENALL",
          "date_commission_decision": null,
          "flag_exparte_allowed": "Y",
          "name": "17-108",
          "date_oral_argument": null,
          "date_reporting_and_order": null,
          "date_hot_docket": null,
          "recent_filings": 2,
          "days": 30,
          "location": " ",
          "rule_section": " ",
          "comment_reply_start_date": null
        }
      ],
      "presented_to": [],
      "date_received": "2017-04-27T20:00:05.188Z",
      "text_data": "The draft seeks comment on the analysis in Paragraph 27. This analysis purports to show that broadband Internet service is an information service because it provides users the \"capability for generating, acquiring, storing, transforming, processing, retrieving, utilizing, or making available information via telecommunications.\" The argument given is that broadband Internet service allows users to do all these things. However, this is not the same as providing the capability to do these things. To see why, consider that providing users Internet services over dialup phone lines also allows users to do all these things; but the phone lines themselves are telecommunications services, not information services. Why? Because providing the user dialup Internet, by itself, does not provide them the capability to do all these things. That capability is provided by the endpoints: the users' computers, and the computers hosting the Internet services that the users connect to.\nExactly the same is true of broadband Internet services provided by ISPs: by themselves, they do not provide users the capability to do all these things. They only provide connections between computers at the endpoints that provide those capabilities. It is the services provided by the Internet hosts that users connect to that are \"information services\". The broadband Internet services that allow users to connect to those hosts are telecommunications services, and should be regulated as such.\nISPs object to analyses like the one above because they claim that they also provide the actual information services--in other words, they also provide Internet hosts that function as email servers, web servers, etc. But it is obvious that those services are separate from the broadband connection services provided by those same ISPs, because users can make use of the latter without making use of the former at all. I am such a user: I use the broadband Internet connection provided by my ISP, but I do not use any of the information services they provide; I do not use their email, their web hosting, etc. I use other Internet hosts provided by other companies for those services. The fact that ISPs offer information services as well as telecommunications services does not make their telecommunications services into information services; an ISP's choice of business model cannot change the nature of a particular service it provides. Broadband Internet connections are obviously a telecommunications service, and should be regulated as such, regardless of what other services ISPs would like to bundle with them. The FCC should continue to regulate broadband Internet service as a telecommunications service.",
      "authors": [],
      "highlight": {
        "text_data": [
          "The draft seeks comment on the analysis in"
        ]
      },
      "_index": "filings.2017.4"
    }