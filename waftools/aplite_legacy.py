from waflib.Configure import conf


@conf
def appinfo_bitmap_to_png(ctx, appinfo_json):
    if hasattr(ctx, 'supports_bitmap_resource') and not ctx.supports_bitmap_resource():
        for res in appinfo_json['resources']['media']:
            if res['type'] == 'bitmap':
                res['type'] = 'png'
