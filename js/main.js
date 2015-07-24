$(function(){
  var $commitsList = $('.commits-list');
  var keyValuePairs = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&");
  var x, params = {};
  $.each(keyValuePairs, function(i, keyValue){
    x = keyValue.split('=');
    params[x[0]] = x[1];
  });

params.owner = "alexhagen";
params.repo = "alexhagen.github.io";

  $.ajax( "https://api.github.com/repos/" + params.owner + "/" + params.repo + "/commits?callback=callback", {
    dataType: 'jsonp',
    type: 'get',
    data: {
      per_page: params.limit || 1
    },
    success: function(response, textStatus, jqXHR) {
      var data = response.data;
      $.each(data, function(i, commit){
        var $li = $('<li></li>').appendTo( $commitsList );
        if( commit.sha && commit.commit && commit.commit.message && commit.commit.author && commit.commit.committer && commit.commit.committer.date ) {
          $right = $('<div></div>').appendTo( $li );
          $('<p class="commit-message"><a href="https://github.com/' + params.owner + '/' + params.repo + '/commit/' + commit.sha + '" target="_blank">' + commit.commit.message + '</a> by <span class="committer-name">' + commit.commit.author.name + '</span> - <span class="commit-time">' + $.timeago(commit.commit.committer.date) + '</span></p>').appendTo( $right );
        } else {
          // Render nothing.  Or render a message:
          // $('<div class="left">&nbsp;</div>').appendTo( $li );
          // $right = $('<div class="right"></div>').appendTo( $li );
          // $('<span class="commit-meta">this commit cannot be rendered</span>').appendTo( $right );
          // $('<div class="clearfix"></div>').appendTo( $li );
        }
      });
    }
  });
});
