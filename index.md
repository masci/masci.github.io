---
layout: home
title: /dev/
subtitle: I'm Massimiliano Pippi, software developer, <em>masci</em> on some services.
---
{% include JB/setup %}

## Writings

<ul class="posts">
  {% for post in site.posts limit: 5 %}
    <li><span>[{{ post.date | date_to_string }}]</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## Open Source Projects

 * [Django Stored Messages](https://github.com/evonove/django-stored-messages) django.contrib.messages on steroids.
 * [Django OAhuth Toolkit](https://github.com/evonove/django-oauth-toolkit) OAuth goodies for the Djangonauts.
 * [This site](https://github.com/masci/masci.github.io) /dev/
 * [Webfactor](https://bitbucket.org/evonove/webfactor) Point and click deploy control tool built with Flask
 * [Milliways](https://bitbucket.org/masci/milliways) The game at the end of the universe

## Follow me

 * [masci]({{ site.author.github }}) on GitHub
 * [maxpippi]({{ site.author.twitter }}) on Twitter
 * [Massimiliano Pippi](https://plus.google.com/MassimilianoPippi) on G+
 * [masci]({{ site.author.flickr }}) on Flickr
 * [Massimiliano Pippi]({{ site.author.linkedin }}) on LinkedIn
 * [masci]({{ site.author.speakerdeck }}) on Speakerdeck
