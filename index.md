---
layout: home
title: /dev/
subtitle: I'm Massimiliano Pippi, software developer, <em>masci</em> on most services.
---
{% include JB/setup %}

## Writings

<ul class="posts">
  {% for post in site.posts limit: 5 %}
    <li><span>[{{ post.date | date_to_string }}]</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>

## Open Source Projects

 * [Project a](http://fava.com)
 * Project b

## Follow me

 * [masci]({{ site.author.github }}) on GitHub
 * [maxpippi]({{ site.author.twitter }}) on Twitter
 * [masci]({{ site.author.flickr }}) on Flickr
 * [Massimiliano Pippi]({{ site.author.linkedin }}) on LinkedIn
