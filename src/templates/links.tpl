
{%extends "layout.tpl" %}


{% block  body %}
<article class="links">
<section>
{% for link in links %}
    <li> <a target="_blank" href="http://"{{ link.url }}> {{link.name }} <li>
{% endfor %}
</section>
</article>

{%endblock %}
