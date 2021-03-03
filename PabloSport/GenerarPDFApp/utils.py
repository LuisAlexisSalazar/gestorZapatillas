# Crear funcion que convierta html a pdf

from xhtml2pdf import pisa
from io import BytesIO

from django.template.loader import get_template
from django.shortcuts import render,HttpResponse

def render_to_pdf(template_src, contex_dic={}):
    # Recuperar el template en base a la ruta que le pasemos
    template=get_template(template_src)

    html=template.render(contex_dic)
    result=BytesIO()

    # La idea del iso.. es convertir en un formato estandar de bytes para que la conversion no sea extraña
    pdf=pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None