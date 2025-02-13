---
title: {name}
search:
  boost: 1
---

<script src="/javascripts/leaderboards.js"></script>

??? note "View Options"
    | Time Format | Date Format |
    | -------     | -- |
    | <input type="button" id="long-time-format" class="md-button md-button--primary" value="Long (1m 00s 000ms)" onclick="LongTime()"/> | <input type="button" id="iso-date-format" class="md-button md-button--primary" value="ISO 8601 (YYYY-MM-DD)" onclick="ISODate()"/>
    | <input type="button" id="wca-time-format" class="md-button" value="WCA (1:00.00)" onclick="ShortTime()"/> | <input type="button" id="relative-date-format" class="md-button" value="Relative (__ days ago)" onclick="RelativeDate()"/> |