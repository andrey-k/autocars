'use strict';
var gulp = require('gulp'),
    less = require('gulp-less'),
    minifyCss = require('gulp-minify-css'),
    uncss = require('gulp-uncss'),
    imagemin = require('gulp-imagemin'),
    uglify = require('gulp-uglify'),
    rename = require("gulp-rename"),
    paths = {
      lessSource: 'django/sections/static/sections/css/base.less',
      lessDest: 'django/sections/static/sections/css',
      jsSource: 'django/sections/static/sections/js/base.js',
      jsDest: 'django/sections/static/sections/js',
      imagesSource: 'img/*',
      imagesDest: 'django/sections/static/sections/img',
      cssLibsSource: 'libs/bootstrap/css/bootstrap.min.css',
      cssLibsDest: 'django/sections/static/sections/libs',
      html: ['django/templates/base.html', 'django/templates/header_footer.html', 'django/sections/templates/sections/index.html']
    };

// Transform .less files to .css and minify it
gulp.task('base-css', function () {
  return gulp.src(paths.lessSource)
    .pipe(less())
    .pipe(minifyCss())
    .pipe(gulp.dest(paths.lessDest));
});

// Compress js and add .min suffix
gulp.task('compress-js', function() {
  return gulp.src(paths.jsSource)
    .pipe(uglify())
    .pipe(rename({suffix: ".min"}))
    .pipe(gulp.dest(paths.jsDest))
});

// Clean bootstrap css
gulp.task('uncss', function() {
  return gulp.src(paths.cssLibsSource)
    .pipe(uncss({
      html: paths.html
    }))
    .pipe(minifyCss())
    .pipe(gulp.dest(paths.cssLibsDest));
});

// Minify images and copy to destination
gulp.task('image-min', function () {
  return gulp.src(paths.imagesSource)
    .pipe(imagemin({}))
    .pipe(gulp.dest(paths.imagesDest));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.lessSource, ['base-css']);
  gulp.watch(paths.jsSource, ['compress-js']);
});

gulp.task('default', ['base-css', 'uncss', 'compress-js']);