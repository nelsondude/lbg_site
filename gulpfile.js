const gulp = require('gulp');
const livereload = require('gulp-livereload');
const sass = require('gulp-sass');

sass.compiler = require('node-sass');

const cssMatch = ['**/*.scss', '!node_modules/**/*.scss'];

gulp.task('scss', function () {
  return gulp.src(cssMatch, {base: './'})
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest(''))
    .pipe(livereload());
});

/* Watch Files For Changes */
gulp.task('watch', function () {
  livereload.listen();
  /* Trigger a live reload on any Django template changes */
  gulp.start('scss');
  gulp.watch('**/*.html').on('change', livereload.changed);
  gulp.watch(cssMatch, ['scss']);
});

gulp.task('default', ['watch']);
