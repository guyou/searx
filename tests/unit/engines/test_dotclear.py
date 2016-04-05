# -*- coding: utf-8 -*-
from collections import defaultdict
import mock
from searx.engines import dotclear
from searx.testing import SearxTestCase


class TestDokuEngine(SearxTestCase):

    def test_request(self):
        query = 'test_query'
        dicto = defaultdict(dict)
        params = dotclear.request(query, dicto)
        self.assertIn('url', params)
        self.assertIn(query, params['url'])

    def test_response(self):
        self.assertRaises(AttributeError, dotclear.response, None)
        self.assertRaises(AttributeError, dotclear.response, [])
        self.assertRaises(AttributeError, dotclear.response, '')
        self.assertRaises(AttributeError, dotclear.response, '[]')

        response = mock.Mock(text='<html></html>')
        self.assertEqual(dotclear.response(response), [])

        html = u"""
<div id="d-main">
<div id="d-content">
  <div id="content-info" class="topbox">
    <h2><a href="https://dotclear.org/blog/">Dotclear News</a> &#187; Search</h2>
          <p>Your search for <em>inex</em> returned no result.</p>
              </div>
</div> <!-- End #d-content -->
</div> <!-- End #d-main -->
        """
        response = mock.Mock(text=html)
        results = dotclear.response(response)
        self.assertEqual(dotclear.response(response), [])

        html = u"""
<div id="d-main">
<div id="d-content">
  <div id="content-info" class="topbox">
    <h2><a href="https://dotclear.org/blog/">Dotclear News</a> &#187; Search</h2>
                  <p>Your search for <em>dotclear 2</em> returned <strong>63</strong> results.</p>
      </div>
      <div class="post odd first">

          <p class="day-date"><span class="dmonth">2016      <span>Mar</span></span>
      <span class="dday">27</span></p>
    <h2 id="p1043" class="post-title"><a
    href="https://dotclear.org/blog/post/2016/03/27/Dotclear-2.9.1">Dotclear 2.9.1</a></h2>
    <p class="post-info">By <a href="http://open-time.net/">Franck</a>    on Sunday 27 March 2016, 11:16        -
<a href="https://dotclear.org/blog/category/News">News</a>
        </p>
          <div class="post-content"><p>A new maintenance release which fixes several bugs of the previous 2.9.
I remind you that Dotclear is fully compatible with the new PHP 7 (it's performances are highly improved comparing
with PHP 5.n)<sup>[<a href="#pnote-1043-1" id="rev-pnote-1043-1">1</a>]</sup>.</p>


<p>Your dashboard should also offer you to upgrade your installation today or tomorrow (depending on your settings).
There's also a <a href="http://download.dotclear.org/patches/2.9-2.9.1.diff.gz">patch</a> for the developers who prefer
this method.</p>
<div class="footnotes"><h4 class="footnotes-title">Note</h4>
<p>[<a href="#rev-pnote-1043-1" id="pnote-1043-1">1</a>] If you use MySQL for your database, take care to use the
<strong>mysqli</strong> driver rather than the old <strong>mysql</strong> which is not more supported by PHP 7
(see in your configuration file <code>inc/config.php</code>).</p></div>
</div>
          <p class="post-info-co">
<a href="https://dotclear.org/blog/post/2016/03/27/Dotclear-2.9.1#comments" class="comment_count">no comment</a>
<a href="https://dotclear.org/blog/post/2016/03/27/Dotclear-2.9.1#pings" class="ping_count">no trackback</a>
             </p>
        </div>
          <div class="post  ">

          <p class="day-date"><span class="dmonth">2016      <span>Feb</span></span>
      <span class="dday">29</span></p>
    <h2 id="p1041" class="post-title"><a
    href="https://dotclear.org/blog/post/2016/02/29/Dotclear-2.9">Dotclear 2.9</a></h2>
    <p class="post-info">By <a href="http://open-time.net/">Franck</a>    on Monday 29 February 2016, 13:17        -
<a href="https://dotclear.org/blog/category/News">News</a>
        </p>
          <div class="post-content"><blockquote><p>My lambs, it's time to update, the new 2.9 version awaits you!</p>
<p>
<em>Fédor Balanovitch</em> (coming out of the bus, almost) — Zazie in the metro, R. Queneau</p></blockquote>


<p>The updated proposal of your installation should appear on your dashboard today or tomorrow
(depending on the settings of your accommodation) and a
<a href="http://download.dotclear.org/patches/2.8.2-2.9.diff.gz">patch</a> is available to developers preferring
to apply this method.</p>
<div class="footnotes"><h4 class="footnotes-title">Notes</h4>
<p>[<a href="#rev-pnote-1041-1" id="pnote-1041-1">1</a>] The jQuery 2.2.0 version is now available for the public
side of your blogs, if necessary.</p>
<p>[<a href="#rev-pnote-1041-2" id="pnote-1041-2">2</a>] Hosting services with less than 5.3 version of PHP begins
hard to find, and it's a good news.</p></div>
</div>
          <p class="post-info-co">
<a href="https://dotclear.org/blog/post/2016/02/29/Dotclear-2.9#comments" class="comment_count">one comment</a>
                      </p>
        </div>
          <div class="post odd ">

          <p class="day-date"><span class="dmonth">2015      <span>Oct</span></span>
      <span class="dday">25</span></p>
    <h2 id="p1039" class="post-title"><a
    href="https://dotclear.org/blog/post/2015/10/25/Dotclear-2.8.2">Dotclear 2.8.2</a></h2>
    <p class="post-info">By <a href="http://open-time.net/">Franck</a>    on Sunday 25 October 2015, 09:41        -
<a href="https://dotclear.org/blog/category/News">News</a>
        </p>
          <div class="post-content">
<p>A new maintenance release which fixes one potential XSS vulnerability in comments's list and enforce media
extension before upload<sup>[<a href="#pnote-1039-1" id="rev-pnote-1039-1">1</a>]</sup>
(thanks to Tim Coen, Curesec Gmbh, for reporting them) and two other bugfixes.</p>


<div class="footnotes"><h4 class="footnotes-title">Note</h4>
<p>[<a href="#rev-pnote-1039-1" id="pnote-1039-1">1</a>] You may also create an <strong>.htaccess</strong>
file at the root of your public folder, with an <strong>php_flag engine Off</strong> directive to prevent any
PHP code execution from your media library.</p></div>
</div>
                        </div>
          <div class="post  ">
          <p class="day-date"><span class="dmonth">2015      <span>Sep</span></span>
      <span class="dday">23</span></p>
    <h2 id="p1037" class="post-title"><a
    href="https://dotclear.org/blog/post/2015/09/23/Dotclear-2.8.1">Dotclear 2.8.1</a></h2>
    <p class="post-info">By <a href="http://open-time.net/">Franck</a>    on Wednesday 23 September 2015, 15:36        -
<a href="https://dotclear.org/blog/category/News">News</a>
        </p>
          <div class="post-content">
<p>A new maintenance release which fixes one potential XSS vulnerabilities
(thanks to Yuji Tounai of NTT Com Security (Japan) KK, via Keiko Yashiki from JPCERT/CC) and two other bugfixes.</p>


<p>Your dashboard should also offer you to upgrade your installation today or tomorrow (depending on your settings).
There's also a <a href="http://download.dotclear.org/patches/2.8-2.8.1.diff.gz">patch</a> for the developers who
prefer this method.</p></div>
                        </div>
</div> <!-- End #d-content -->
</div> <!-- End #d-main -->

        """
        response = mock.Mock(text=html)
        results = dotclear.response(response)
        self.assertEqual(type(results), list)
        self.assertEqual(len(results), 4)
        self.assertEqual(results[0]['title'], 'Dotclear 2.9.1')
# FIXME        self.assertEqual(results[0]['url'], u'http://this.should.be.the.link/ű')
# FIXME        self.assertEqual(results[0]['content'], 'This should be the content.')
