#! /usr/bin/python

import os
import pdfrw


TEMPLATE_PATH = 'final_template_4real.pdf'
OUTPUT_PATH = 'final_file2.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(AP='', V='{}'.format(data_dict[key]), AS=pdfrw.PdfName("Yes"))
                    )
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


def write_fillable_pdf2(input_pdf_path, output_pdf_path, data_dict):

    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V=pdfrw.PdfName.Yes, AS=pdfrw.PdfName.On, AP=pdfrw.PdfName.Yes)
                    )
                    print(pdfrw.PdfDict(V=pdfrw.PdfName.Yes, AS=pdfrw.PdfName.On, AP=pdfrw.PdfName.On))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


def create_dict2():

    data_dict2 = {
        'where applicable': pdfrw.PdfName.No,
        'New Registration': pdfrw.PdfName.Yes,
        'Record UpdateChange eg Address Party Affiliation Name Signature': pdfrw.PdfName.Yes,
        'Request to Replace Voter Information Card': "/On",
        'Are you a citizen of the United States of America': 'On',  # or NO
        'I affirm I have never been convicted of a felony': '1',
        'If I have been convicted of a felony I affirm my voting rights have been restored by': '1',
        'If I have been convicted of a felony I affirm my voting rights have been restored': '1',
        'I affirm that I have not been adjudicated': '1',
        'Email me SAMPLE BALLOTS': 'Y',
        'Florida Democratic Party': 'Y',
        'Republican Party of Florida': '',
        'No party affiliation': '',
        'Minor party print party name': '',
        'American IndianAlaskan Native': '',
        'AsianPacific Islander': '',
        'Black not of Hispanic Origin': '',
        'Hispanic': '/On',
        'White not of Hispanic Origin': '',
        'Multiracial': '',
        'I am an active duty Uniformed Services or Merchant': True,
        'I am a spouse or a dependent of an active duty uniformed': True,
        'I am a US citizen residing outside the US': "Yes",
        'I will': 'Y',
        'I am': 'Y',
        'undefined_party': '',
        'undefined_Race': '',
    }
    return data_dict2

def create_dict():

        data_dict = {
            'where applicable': 0,
            'New Registration': 1,
            'Record UpdateChange eg Address Party Affiliation Name Signature': "Yes",
            'Request to Replace Voter Information Card': 'On',
            'Are you a citizen of the United States of America': 'On',  # or NO
            'I affirm I have never been convicted of a felony': '1',
            'If I have been convicted of a felony I affirm my voting rights have been restored by': '1',
            'If I have been convicted of a felony I affirm my voting rights have been restored': '1',
            'I affirm that I have not been adjudicated': '1',
            'MM': '0',
            'MM_2': '1',
            'DD': '1',
            'DD_2': '1',
            'Y': '2',
            'YY': '0',
            'YYY': '1',
            'YYYY': '9',
            'FLFL': '1',
            'FLFL_2': '2',
            'FLFL_3': '3',
            'FLFL_4': '4',
            'FLFL_5': '5',
            'FLFL_6': '6',
            'FLFL_7': '7',
            'FLFL_8': '8',
            'FLFL_9': '9',
            'FLFL_10': '0',
            'FLFL_11': '1',
            'FLFL_12': '2',
            'FLFL_13': '3',
            'SS': '2',
            'SS_2': '3',
            'SS_3': '4',
            'SS_4': '5',
            'Last Name': 'der',
            'First Name': request.form['firstname'],#'bob',
            'Middle Name': 'b.',
            'numbers': 'sr.',
            'Address Where You Live legal residenceno PO Box': '123',
            'AptLotUnit': 'vfr',
            'City': 'chester',
            'County': 'brevard',
            'Zip Code': '19425',
            'Mailing Address if different from above address': '',
            'AptLotUnit_2': '',
            'City_2': '',
            'County_2': '',
            'Zip Code_2': '',
            'Address Where You Were Last Registered to Vote': 'bongo',
            'AptLotUnit_3': '6',
            'City_3': 'mars',
            'State': 'universe',
            'Zip Code_3': '001010',
            'Former Name if name is changed': 'paul blart',
            'Gender': 'Male',
            'State or Country of Birth': 'USA',
            'Area Code':'321',
            'Telephone No Prefix':'423',
            'Telephone No Subscriber':'1338',
            'undefined_2': '2',
            'Email me SAMPLE BALLOTS': 'Y',
            'Florida Democratic Party': 'Y',
            'Republican Party of Florida': '',
            'No party affiliation': '',
            'Minor party print party name': '',
            'American IndianAlaskan Native': '',
            'AsianPacific Islander': '',
            'Black not of Hispanic Origin': '',
            'Hispanic': 'Y',
            'White not of Hispanic Origin': '',
            'Multi-racial': "/On",
            'Other': '',
            'I am an active duty Uniformed Services or Merchant': True,
            'I am a spouse or a dependent of an active duty uniformed': True,
            'I am a US citizen residing outside the US': "Yes",
            'I will': 'Y',
            'I am': 'Y',
            'undefined_party': '',
            'undefined_Race': '',
            'SIGN MARK HERE': 'sdddd',
            'Signature': 'Alex Winstead',
            'Date': '9/21/19'
        }
        return data_dict


def main(timestamp, dictionary):
    #write_fillable_pdf2(TEMPLATE_PATH, OUTPUT_PATH, create_dict())
    write_fillable_pdf(TEMPLATE_PATH, "forms/" + timestamp+".pdf", dictionary)
